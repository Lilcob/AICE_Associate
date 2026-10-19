import numpy as np
import pandas as pd
from time import perf_counter
demo = pd.DataFrame({
    'group': np.tile(['A', 'B', 'C', 'D'], 5000),
    'value': np.arange(20000, dtype=float)
})
cat_demo = demo.copy()
cat_demo['group'] = cat_demo['group'].astype('category')
for name, frame in [('원본', demo), ('category', cat_demo)]:
    print(name, frame.memory_usage(deep=True).sum(), 'bytes')
    start = perf_counter()
    result = frame.groupby('group', observed=True)['value'].mean()
    print(result)
    print(f'그룹화 시간: {perf_counter() - start:.6f}초')
