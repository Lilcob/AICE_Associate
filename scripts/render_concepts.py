from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle,FancyArrowPatch
B=Path(__file__).resolve().parents[1];OUT=B/'assets/concepts';OUT.mkdir(parents=True,exist_ok=True)
font=Path('/System/Library/Fonts/Supplemental/AppleGothic.ttf')
font_manager.fontManager.addfont(str(font));family=font_manager.FontProperties(fname=str(font)).get_name()
plt.rcParams.update({'font.family':family,'font.size':10.5,'axes.unicode_minus':False,'pdf.fonttype':42,'svg.fonttype':'path'})
INK='#243746';BLUE='#2D6B9C';PALE='#EAF2F8';GRAY='#61717D';ORANGE='#B8652A';GRID='#AEBCC5'
manifest=[]
def canvas(title,height=3.6):
 f=plt.figure(figsize=(6.2,height),facecolor='white');a=f.add_axes([.035,.035,.93,.93]);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off');a.text(.5,.97,title,ha='center',va='top',fontsize=15,color=INK);return f,a

def text(a,x,y,s,size=10.5,color=INK,ha='center',va='center',**kw):
 return a.text(x,y,s,fontsize=size,color=color,ha=ha,va=va,linespacing=1.35,**kw)
def matrix(a,x,y,data,w=.27,h=.32,header=None,high=None):
 rows=len(data);cols=len(data[0]);cw=w/cols;rh=h/rows
 for i,row in enumerate(data):
  for j,val in enumerate(row):
   fill=PALE if (high and i in high) else 'white'
   if header and i==0:fill='#F0F3F5'
   a.add_patch(Rectangle((x+j*cw,y-(i+1)*rh),cw,rh,facecolor=fill,edgecolor=GRID,linewidth=.8))
   text(a,x+(j+.5)*cw,y-(i+.5)*rh,str(val),size=10.5)
def arrow(a,x,y,x2,y2):a.add_patch(FancyArrowPatch((x,y),(x2,y2),arrowstyle='-|>',mutation_scale=13,color=BLUE,linewidth=1.5))
def save(f,name,anchor,caption,transition,alt):
 for ext in ['png','svg','pdf']:f.savefig(OUT/(name+'.'+ext),dpi=300)
 # Check every visible label stays within the figure; axes text may use normalized positions.
 f.canvas.draw();ren=f.canvas.get_renderer();bounds=f.bbox
 for obj in f.findobj(match=matplotlib.text.Text):
  if not obj.get_visible() or not obj.get_text():continue
  box=obj.get_window_extent(ren)
  assert box.x0>=bounds.x0-.5 and box.y0>=bounds.y0-.5 and box.x1<=bounds.x1+.5 and box.y1<=bounds.y1+.5,(name,obj.get_text(),box.bounds)
 manifest.append({'name':name,'anchor_id':anchor,'png':str((OUT/(name+'.png')).resolve()),'caption':caption,'transition':transition,'alt':alt,'size_in':list(f.get_size_inches()),'kind':'conceptual_teaching_illustration'})
 plt.close(f)

f,a=canvas('브로드캐스팅은 오른쪽 차원부터 맞춥니다',3.4)
text(a,.5,.81,'(2, 3)  +  (3,)  →  (2, 3)',size=13,color=BLUE)
matrix(a,.015,.66,[[1,2,3],[4,5,6]],w=.27,h=.30)
text(a,.32,.52,'+',size=19)
matrix(a,.365,.66,[[10,20,30],[10,20,30]],w=.27,h=.30,high={0,1})
text(a,.67,.52,'=',size=19)
matrix(a,.715,.66,[[11,22,33],[14,25,36]],w=.27,h=.30)
text(a,.5,.28,'[10, 20, 30]이 각 행에 대응한다고 생각합니다.',size=10.5)
text(a,.5,.13,'같은 크기이거나 한쪽이 1이어야 합니다.\n(2, 3) + (2,)는 마지막 차원 3과 2가 달라 오류가 납니다.',size=10.5)
save(f,'broadcasting',228,'작은 배열이 각 행에 대응하는 브로드캐스팅 예시. 배열을 실제로 반복 복사한다는 뜻은 아닙니다.','배열을 더하기 전에 shape의 오른쪽 끝부터 비교해보겠습니다.','2행3열 배열에 길이3의 배열을 더하면 각 행에 10,20,30이 더해져 11,22,33과14,25,36이 됩니다. 길이2 배열은 마지막 차원이 달라 더할 수 없습니다.')

f,a=canvas('loc는 레이블, iloc는 위치로 선택합니다',3.7)
values=[['인덱스','A','B'],['x (0)','1','4'],['y (1)','2','5'],['z (2)','3','6']]
matrix(a,.025,.77,values,w=.43,h=.40,header=True,high={2,3})
matrix(a,.545,.77,values,w=.43,h=.40,header=True,high={2})
text(a,.24,.27,"loc['y':'z']",size=13,color=BLUE)
text(a,.76,.27,'iloc[1:2]',size=13,color=BLUE)
text(a,.24,.16,'끝 레이블 z 포함\ny, z 두 행',size=11)
text(a,.76,.16,'끝 위치 2 제외\ny 한 행',size=11)
text(a,.5,.045,'괄호 속 숫자는 0부터 시작하는 위치입니다. 원래 인덱스는 x, y, z입니다.',size=9.8,color=GRAY)
save(f,'loc_iloc',1125,'같은 표에서 loc의 레이블 슬라이스와 iloc의 위치 슬라이스를 비교합니다.','loc와 iloc는 선택 기준뿐 아니라 슬라이스의 끝을 포함하는지도 다릅니다.','행 레이블 x,y,z와 위치0,1,2가 있는 동일한 표에서 loc의 y:z는 y,z 두 행을, iloc의1:2는 위치1인 y만 선택합니다.')

f,a=canvas('merge는 공통 키를 기준으로 행을 연결합니다',4.45)
text(a,.23,.83,'왼쪽: 고객',size=11,color=BLUE);text(a,.77,.83,'오른쪽: 이용량',size=11,color=BLUE)
matrix(a,.03,.77,[['ID','이름'],[101,'가'],[102,'나'],[103,'다']],w=.40,h=.27,header=True)
matrix(a,.57,.77,[['ID','사용량'],[102,20],[103,30],[104,40]],w=.40,h=.27,header=True)
arrow(a,.23,.48,.23,.40);arrow(a,.77,.48,.77,.40)
text(a,.23,.36,"how='inner'",size=12,color=BLUE);text(a,.77,.36,"how='left'",size=12,color=BLUE)
matrix(a,.005,.31,[['ID','이름','사용량'],[102,'나',20],[103,'다',30]],w=.47,h=.20,header=True)
matrix(a,.525,.31,[['ID','이름','사용량'],[101,'가','NaN'],[102,'나',20],[103,'다',30]],w=.47,h=.20,header=True,high={1})
text(a,.5,.045,'이 예시는 키가 고유합니다. 키가 중복되면 결과 행 수가 늘 수 있습니다.',size=10.2,color=GRAY)
save(f,'merge_keys',1540,'공통 키만 남기는 inner와 왼쪽 키를 유지하는 left의 차이. 일치하는 오른쪽 값이 없으면 NaN이 들어갑니다.','병합 방식을 고를 때는 어떤 키를 남길지 먼저 정합니다. 아래 그림은 키가 중복되지 않는 작은 예시입니다.','왼쪽ID101,102,103과 오른쪽ID102,103,104를 병합하면 inner에는102,103만 남고 left에는101,102,103이 남습니다.101의 사용량은 NaN입니다.')

f,a=canvas('원핫 인코딩은 훈련 범주와 열 순서를 유지합니다',4.15)
text(a,.5,.83,"훈련에서 fit  →  categories_: blue, green, red",size=11.5,color=BLUE)
matrix(a,.12,.73,[['입력','blue','green','red'],['red',0,0,1],['blue',1,0,0],['green',0,1,0]],w=.76,h=.32,header=True)
arrow(a,.5,.38,.5,.29)
text(a,.5,.24,"검증에서 transform: yellow  →  [0, 0, 0]",size=11.5)
text(a,.5,.12,"drop=None, handle_unknown='ignore'인 예시입니다.\n훈련 때 없던 yellow를 만나도 새로운 열을 만들지 않습니다.",size=10.5,color=GRAY)
save(f,'onehot_columns',3526,'훈련 자료에서 정한 범주·열 순서로 검증 자료를 변환합니다. 미지 범주 처리는 인코더 설정에 따라 달라집니다.','원-핫 인코딩 결과는 열 이름과 순서까지 모델 입력의 일부입니다. 훈련에 없던 범주가 들어오면 어떻게 처리되는지도 확인하세요.','훈련범주blue,green,red가세열이됩니다.red는001,blue는100,green은010입니다. handle_unknown ignore와drop None 설정에서 새범주yellow는 같은세열에000으로 변환됩니다.')

f,a=canvas('문제와 정답 형식에 맞춰 출력층과 손실을 고릅니다',3.5)
rows=[['문제','정답 y','출력층','손실함수'],['회귀','연속값','Dense(1)\nlinear','mse'],['이진 분류','0 또는 1','Dense(1)\nsigmoid','binary_crossentropy'],['다중 분류','정수 클래스\n0, 1, …, K-1','Dense(K)\nsoftmax','sparse_categorical_\ncrossentropy'],['다중 분류','원핫 벡터\n길이 K','Dense(K)\nsoftmax','categorical_crossentropy']]
tbl=a.table(cellText=rows,cellLoc='center',colWidths=[.15,.21,.24,.40],bbox=[.0,.18,1,.64])
for (i,j),cell in tbl.get_celld().items():
 cell.set_edgecolor(GRID);cell.set_linewidth(.7);cell.set_facecolor('#F0F3F5' if i==0 else 'white');cell.set_text_props(fontsize=10,color=INK)
tbl.auto_set_font_size(False)
text(a,.5,.065,'K는 클래스 수입니다. 분류 예시는 확률 출력과 from_logits=False 기준입니다.',size=10.2,color=GRAY)
save(f,'output_loss',4315,'같은 다중 분류라도 정수 라벨과 원-핫 라벨은 사용하는 손실함수가 다릅니다.','출력층·정답 라벨·손실함수는 한 세트로 맞춰야 합니다. 다음 표형 그림으로 선택 기준을 확인해보겠습니다.','회귀는연속정답과선형출력MSE, 이진분류는0/1정답sigmoid출력binarycrossentropy, 다중분류는softmaxK개출력이며 정수라벨은sparsecategoricalcrossentropy, 원핫라벨은categoricalcrossentropy입니다.')

f=plt.figure(figsize=(6.2,3.6),facecolor='white')
f.suptitle('학습 곡선은 훈련과 검증을 함께 읽습니다',fontsize=15,color=INK,y=.97)
x=np.linspace(1,30,30);train=.70*np.exp(-x/12)+.08
valid_good=.70*np.exp(-x/12)+.18
valid_bad=.77*np.exp(-x/7)+.15+.018*np.maximum(x-11,0)
for k,(v,title) in enumerate([(valid_good,'두 손실이 함께 감소'),(valid_bad,'검증 손실이 지속적으로 상승')]):
 ax=f.add_axes([.10+k*.47,.27,.38,.48]);ax.plot(x,train,label='Training',color=BLUE,lw=2);ax.plot(x,v,label='Validation',color=ORANGE,lw=2)
 ax.set_title(title,fontsize=10.5,pad=9);ax.set_xlabel('Epoch');ax.set_ylabel('Loss');ax.set_xticks([]);ax.set_yticks([]);ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
 if k==0:ax.legend(fontsize=9,frameon=False,loc='upper right')
 else:
  best=np.argmin(v);ax.scatter(x[best],v[best],color=ORANGE,zorder=5);ax.axvline(x[best],color=GRAY,ls=':',lw=1)
  ax.text(.5,.92,'과적합 가능성 점검',transform=ax.transAxes,ha='center',fontsize=9.5,color=ORANGE)
f.text(.5,.11,'관측 결과가 아닌 경향을 설명하는 개념도입니다.\n한 번의 상승으로 판단하지 말고 데이터 분포·표본 수와 함께 확인합니다.',ha='center',fontsize=10,color=GRAY,linespacing=1.4)
save(f,'learning_curves',4352,'훈련 손실이 줄어도 검증 손실이 지속적으로 오르면 과적합 가능성을 점검합니다.','과적합은 훈련 손실 하나로 판단하지 않습니다. 두 곡선의 추이를 함께 살펴보겠습니다.','왼쪽은훈련과검증손실이함께감소하는경향, 오른쪽은훈련손실은감소하지만검증손실이지속상승하는경향을보이는개념도입니다. 실제학습결과가아닙니다.')

# Numerical/semantic facts used in the diagrams.
a=np.array([[1,2,3],[4,5,6]]);v=np.array([10,20,30]);assert (a+v).tolist()==[[11,22,33],[14,25,36]]
try:a+np.array([10,20]);raise AssertionError('expected mismatch')
except ValueError:pass
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]},index=['x','y','z']);assert df.loc['y':'z'].index.tolist()==['y','z'] and df.iloc[1:2].index.tolist()==['y']
left=pd.DataFrame({'ID':[101,102,103],'이름':['가','나','다']});right=pd.DataFrame({'ID':[102,103,104],'사용량':[20,30,40]})
assert left.merge(right,on='ID',how='inner').ID.tolist()==[102,103]
assert pd.isna(left.merge(right,on='ID',how='left').iloc[0]['사용량'])
enc=OneHotEncoder(handle_unknown='ignore',sparse_output=False);z=enc.fit_transform(pd.DataFrame({'색':['red','blue','green']}));assert enc.categories_[0].tolist()==['blue','green','red'] and z.tolist()==[[0,0,1],[1,0,0],[0,1,0]]
assert enc.transform(pd.DataFrame({'색':['yellow']})).tolist()==[[0,0,0]]
(OUT/'concepts_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(len(manifest),'concept figures; labels and numerical examples checked')
