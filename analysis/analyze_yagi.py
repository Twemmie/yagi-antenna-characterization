import numpy as np,pandas as pd,matplotlib.pyplot as plt
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=root/'results'/'data'
plot_out=root/'results'/'plots'
out.mkdir(parents=True,exist_ok=True)
plot_out.mkdir(parents=True,exist_ok=True)
a=np.arange(0,360,30)
# Five recorded sweeps are loaded from the committed raw measurement table.
df=pd.read_csv(out/'yagi_five_sweeps_raw.csv',index_col='angle_deg')
df.index=df.index.astype(int);df.index.name='angle_deg'
a=df.index.to_numpy()
rel=df.subtract(df.loc[0],axis='columns')
# preserve missing values and don't mix linear/mixed averages
stats=pd.DataFrame({'n':rel.count(axis=1),'mean_rel_0deg_db':rel.mean(axis=1),'median_rel_0deg_db':rel.median(axis=1),'sd_between_sweeps_db':rel.std(axis=1,ddof=1),'min_rel_0deg_db':rel.min(axis=1),'max_rel_0deg_db':rel.max(axis=1)})
summary=[]
for k in df:
 x=df[k].dropna();head=x.loc[[0,30,60,90,120,150]]
 summary.append({'sweep':k,'n':len(x),'p0_db':x.loc[0],'peak_deg':int(x.idxmax()),'peak_db':x.max(),'min_deg':int(x.idxmin()),'min_db':x.min(),'dynamic_range_db':x.max()-x.min(),'front_minus_back_db':x.loc[0]-x.loc[180],'first_half_span_db':head.max()-head.min()})
summ=pd.DataFrame(summary)
# arithmetic mean of log differences is geom. mean ratio; fine with label
for name,data in [('yagi_five_sweeps_raw.csv',df),('yagi_five_sweeps_relative_to_0deg.csv',rel),('yagi_angle_statistics.csv',stats)]:data.to_csv(out/name,float_format='%.6f')
summ.to_csv(out/'yagi_sweep_summary.csv',index=False,float_format='%.6f')
plt.figure(figsize=(11,6.5))
for name in rel:plt.plot(a,rel[name],marker='o',lw=1.7,label=name)
plt.axhline(0,color='gray',alpha=.6,lw=1);plt.xticks(a);plt.xlabel('Physical Yagi orientation (degrees)');plt.ylabel('Integrated received power relative to 0° (dB)');plt.title('Indoor Yagi characterization — 5 physical sweeps (0° referenced)');plt.grid(alpha=.3);plt.legend(ncol=3);plt.tight_layout();plt.savefig(plot_out/'yagi_five_sweeps_overlay.png',dpi=200);plt.close()
plt.figure(figsize=(11,6.5))
plt.errorbar(a,stats['mean_rel_0deg_db'],yerr=stats['sd_between_sweeps_db'],fmt='o-',capsize=4,label='Mean ± 1 between-sweep SD')
plt.axhline(0,color='gray',lw=1,alpha=.6);plt.xticks(a);plt.xlabel('Physical Yagi orientation (degrees)');plt.ylabel('Received power relative to 0° (dB)');plt.title('Across-sweep relative response: mean and between-sweep variability');plt.grid(alpha=.3);plt.legend();plt.tight_layout();plt.savefig(plot_out/'yagi_mean_sd_by_angle.png',dpi=200);plt.close()
print('SUMMARY\n',summ.round(3).to_string(index=False));print('\nSTATS\n',stats.round(3).to_string());
print('\n0-150 across sweep normalized span',[(k,round((df[k].iloc[:6].max()-df[k].iloc[:6].min()),4)) for k in df]);
print('mean front-back',summ.front_minus_back_db.mean(),'sd',summ.front_minus_back_db.std(ddof=1));
print('0 baseline range',df.loc[0].max()-df.loc[0].min());
print('angle 270',rel.loc[270].to_dict());
