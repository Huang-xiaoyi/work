import pandas
import numpy

dates = pandas.date_range("20130101", periods=6)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')


df = pandas.DataFrame(numpy.random.randn(6, 4), index=dates, columns=list("ABCD"))
#index决定行头，columns决定列头
input(df)
pd= pandas.Series(df[0:2])
input(pd)
