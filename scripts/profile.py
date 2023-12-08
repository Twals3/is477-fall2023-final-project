from ydata_profiling import ProfileReport

df = pd.DataFrame()

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("report.html")