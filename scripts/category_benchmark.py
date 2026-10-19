"""Compare category memory/groupby on the same generated data; no fixed speed claim."""
from __future__ import annotations
import argparse,json,time
import numpy as np
import pandas as pd

def benchmark(rows=200_000,repeat=3):
    rng=np.random.default_rng(42)
    df=pd.DataFrame({'cat1':rng.integers(0,100,rows),'cat2':rng.integers(0,50,rows),
                     '성별':rng.choice(['남','여'],rows),'요일':rng.choice(['월','화','수','목','금','토','일'],rows),
                     'value':rng.normal(100,20,rows)})
    begin=time.perf_counter();category=df.copy()
    for col in ['cat1','cat2','성별','요일']:category[col]=category[col].astype('category')
    conversion=time.perf_counter()-begin
    report={'rows':rows,'repeat':repeat,'pandas':pd.__version__,'numpy':np.__version__,
            'memory_MB_original':float(df.memory_usage(deep=True).sum()/1024**2),
            'memory_MB_category':float(category.memory_usage(deep=True).sum()/1024**2),
            'copy_and_conversion_seconds':conversion,'groupby':{}}
    for cols,label in [(['cat1','cat2'],'integer_keys'),(['성별','요일'],'string_keys')]:
        times={}
        results=[]
        for frame,kind in [(df,'original'),(category,'category')]:
            elapsed=[]
            for _ in range(repeat):
                begin=time.perf_counter()
                result=frame.groupby(cols,observed=True,sort=True)['value'].mean()
                elapsed.append(time.perf_counter()-begin)
            times[kind+'_seconds']=elapsed
            results.append(result.reset_index().astype({col:str for col in cols}).sort_values(cols).reset_index(drop=True))
        assert results[0][cols].equals(results[1][cols])
        assert np.allclose(results[0]['value'],results[1]['value'])
        times['groups']=len(results[0]);times['same_aggregation']=True
        report['groupby'][label]=times
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--rows',type=int,default=200_000);parser.add_argument('--repeat',type=int,default=3);args=parser.parse_args()
    if args.rows<1 or args.repeat<1:parser.error('rows and repeat must be positive')
    print(json.dumps(benchmark(args.rows,args.repeat),ensure_ascii=False,indent=2))
