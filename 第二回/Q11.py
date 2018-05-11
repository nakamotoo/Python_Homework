#問11 line1とline2の乗り継ぎ
import galaxyExpresses

line1 = galaxyExpresses.line1()
line2 = galaxyExpresses.line2()

station = set(line1)&set(line2)

print( str(station) + "で乗り継げばいい" )
