import numpy as np,pandas as pd,matplotlib.pyplot as plt
from pathlib import Path
out=Path('/mnt/data')
a=np.arange(0,360,30)
s={
'Sweep 1':[18.35449659786788,18.34224519123588,18.33609444690741,18.317762439413702,18.29728955288299,18.287059836159276,16.536955203367594,7.97145456828673,13.01951487225965,18.433972354309514,20.742717558864044,np.nan],
'Sweep 2':[17.896391820083938,17.89055947924385,17.91855625797726,17.899279392769955,17.890709262595582,17.894279463885276,18.603456520382473,14.103954109815922,8.09856633888421,6.547176783904657,14.30229338227467,13.692094852312009],
'Sweep 3':[17.418086000709497,17.429749262256628,17.433001484262086,17.420891976345935,17.42558886248607,17.428823625270706,14.508836060867887,16.496049174571205,17.445368839515627,18.223436845292753,18.46105933512244,19.28614515517542],
'Sweep 4':[20.81688891376766,20.82830046765103,20.819216584094736,20.813955976952002,20.806230567102077,20.805052817146695,7.638148316744774,10.043799357449467,9.9934780886344,6.464286318447189,12.454119304066097,13.207189402364959],
'Sweep 5':[12.186236488787113,12.201559079780234,12.248104210710014,12.254313078276715,12.233285072139141,12.216137495299309,11.31748555626726,11.991631533287727,9.489849005039684,12.325637669971359,12.435812236114863,14.924919500887569],}
df=pd.DataFrame(s,index=a);df.index.name='angle_deg'
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
plt.axhline(0,color='gray',alpha=.6,lw=1);plt.xticks(a);plt.xlabel('Physical Yagi orientation (degrees)');plt.ylabel('Integrated received power relative to 0° (dB)');plt.title('Indoor Yagi characterization — 5 physical sweeps (0° referenced)');plt.grid(alpha=.3);plt.legend(ncol=3);plt.tight_layout();plt.savefig(out/'yagi_five_sweeps_overlay.png',dpi=200);plt.close()
plt.figure(figsize=(11,6.5))
plt.errorbar(a,stats['mean_rel_0deg_db'],yerr=stats['sd_between_sweeps_db'],fmt='o-',capsize=4,label='Mean ± 1 between-sweep SD')
plt.axhline(0,color='gray',lw=1,alpha=.6);plt.xticks(a);plt.xlabel('Physical Yagi orientation (degrees)');plt.ylabel('Received power relative to 0° (dB)');plt.title('Across-sweep relative response: mean and between-sweep variability');plt.grid(alpha=.3);plt.legend();plt.tight_layout();plt.savefig(out/'yagi_mean_sd_by_angle.png',dpi=200);plt.close()
print('SUMMARY\n',summ.round(3).to_string(index=False));print('\nSTATS\n',stats.round(3).to_string());
print('\n0-150 across sweep normalized span',[(k,round((df[k].iloc[:6].max()-df[k].iloc[:6].min()),4)) for k in df]);
print('mean front-back',summ.front_minus_back_db.mean(),'sd',summ.front_minus_back_db.std(ddof=1));
print('0 baseline range',df.loc[0].max()-df.loc[0].min());
print('angle 270',rel.loc[270].to_dict());
