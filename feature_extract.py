import csv
import math

#def main():
r = open('mouse_data.csv')
csv_r = csv.reader(r)


entry_id = []
session_id = []
timestamp = []
xpos = []
ypos = []
events = []
for row in csv_r:
	entry_id.append(row[0])
	events.append(row[1])
	session_id.append(row[2])
	timestamp.append(float(row[3]))
	xpos.append(int(row[4]))
	ypos.append(int(row[5]))


size = len(entry_id)
#Feature vector array: angle, angular velocity, curvature, curvature change rate, x/y velocity, speed, acceleration, jerk 
dt = [0]
dx = [0]
dy = [0]
ds = [0]

angle = [0]
angle_v = [0]
curve = [0]
curve_r = [0]

vx = [0]
vy = [0]
v = [0]
dvx = [0]
dvy = [0]
dv = [0]
a = [0]
jerk = [0]

#Feature characteristics
#x_min = xpos[0]
#x_max = xpos[0]
#x_mean = [0]
#x_sd = [0]
#x_minmax = [0]
#y_min = ypos[0]
#y_max = ypos[0]
#y_mean = [0]
#y_sd = [0]
#y_minmax = [0]
dy_temp = int(ypos[1]) - int(ypos[0])
dx_temp = int(xpos[1]) - int(xpos[0])
dt_temp = timestamp[1] - timestamp[0]
angle_min = [math.atan2(dy_temp,dx_temp)]
angle_max = [math.atan2(dy_temp,dx_temp)]
angle_mean = [0]
angle_sd = [0]
angle_minmax = [0]
angle_v_min = [(math.atan2(dy_temp,dx_temp) - angle_min[0]) / dt_temp]
angle_v_max = [angle_v_min[0]]
angle_v_mean = [0]
angle_v_sd = [0]
angle_v_minmax = [0]
curve_min = [(math.atan2(dy_temp,dx_temp) - angle_min[0]) / math.sqrt( (dx_temp ** 2) + (dy_temp ** 2))]
curve_max = [curve_min[0]]
curve_mean = [0]
curve_sd = [0]
curve_minmax = [0]
curve_r_min = [curve_min[0] / math.sqrt( (dx_temp ** 2) + (dy_temp ** 2))]	
curve_r_max = [curve_r_min[0]]
curve_r_mean = [0]
curve_r_sd = [0]
curve_r_minmax = [0]
vx_min = [dx_temp / dt_temp]
vx_max = [vx_min[0]]
vx_mean = [0]
vx_sd = [0]
vx_minmax = [0]
vy_min = [dy_temp / dt_temp]
vy_max = [vy_min[0]]
vy_mean = [0]
vy_sd = [0]
vy_minmax = [0]
v_min = [math.sqrt((dx_temp ** 2) + (dy_temp ** 2) / dt_temp)]
v_max = [v_min[0]]
v_mean = [0]
v_sd = [0]
v_minmax = [0]
a_min = [v_min[0] / dt_temp]
a_max = [a_min[0]]
a_mean = [0]
a_sd = [0]
a_minmax = [0]
jerk_min = [a_min[0] / dt_temp]
jerk_max = [jerk_min[0]]
jerk_mean = [0]
jerk_sd = [0]
jerk_minmax = [0]

total_distance = [0]
#total_time = timestamp[size-1]
critical_points = [0]
straightness = [0]
jitter = [0]
strokes = 0	#number of strokes so far
stroke_locations = []	#holds stroke locations
events_complex = [] #holds complex  events
event = 0	#temporary holder
silence = [] #length of each silence
silence_locations = [] #locations of each silence
#mouse_event = []
#extracts features
for i in range(size - 1):
	dt.append(timestamp[i+1] - timestamp[i])
	#determines strokes, based on silence and clicks
	if event == 0 :
		stroke_locations.append(i+1)
		
		
		
	#determines event
	if events[i+1] == "ld":
		strokes += 1	
		event = "ld"
		if events_complex[strokes-2] == "mm" :
			event = "mm_ld"
			#strokes -=1
			
	elif events[i+1] == "lu":
		if event == "mm_ld" :
			event = "mm_lc"
		elif len(events_complex) > 1 :
			if event == "ld" and events_complex[strokes-2] == "lc" :
				events_complex[strokes-2] = "dlc"
				stroke_locations.pop(strokes-1)
				strokes -= 1
				event = 0
			elif event == "ld" and events_complex[strokes-2] == "mm_lc" :
				events_complex[strokes-2] = "mm_dlc"
				stroke_locations.pop(strokes-1)
				strokes -= 1
				event = 0
		elif event == "ld" :
			event = "lc"
	
		if event != 0 :
			events_complex.append(event)
			event = 0
			
	elif events[i+1] == "mm" :
		if event == 0 :
			event = "mm"
			strokes += 1
		if event == "ld" :
			event = "dd"
		elif event == "mm_ld" :
			event = "mm_dd"
		if i+2 < size-1 :
			if events[i+2] == "ld" :
				events_complex.append(event)
				event = 0
			
	if i == size-2 :
		events_complex.append(event)
	
	if dt[i+1] > 50 :
		angle.append(0)
		angle_v.append(0)
		curve.append(0)
		curve_r.append(0)
		vx.append(0)
		vy.append(0)
		v.append(0)
		dvx.append(0)
		dvy.append(0)
		dv.append(0)
		a.append(0)
		jerk.append(0)
		dx.append(0)
		dy.append(0)
		ds.append(0)
		silence.append(dt[i+1])
		silence_locations.append(i)
		
		if event == "mm" :
			events_complex.append("mm")
			event = 0
		#else :
		
	if dt[i+1] <= 50 :
		dx.append(xpos[i+1] - xpos[i])
		#if xpos[i+1] < x_min :
		#	x_min = xpos[i+1]
		#	elif xpos[1] > x_max :
		#	x_max = xpos[i+1]
		#x_mean += xpos[i+1]

		dy.append(ypos[i+1] - ypos[i])
		#if ypos[i+1] < y_min :
		#	y_min = ypos[i+1]
		#elif ypos[i+1] > y_max :
		#	y_max = ypos[i+1]
		#y_mean += ypos[i+1]

		ds.append(math.sqrt((dy[i+1] ** 2) + (dx[i+1] ** 2))) #
		
	
		angle.append(math.atan2(dy[i+1],dx[i+1])) #

		angle_v.append((angle[i+1] - angle[i]) / dt[i+1])
		
		
		if ds[i+1] == 0 :
			curve.append(0)
		else :
			curve.append((angle[i+1] - angle[i]) / ds[i+1])
			

		if ds[i+1] == 0 :
			curve_r.append(0)
		else :
			curve_r.append((curve[i+1] - curve[i]) / ds[i+1])
			

		vx.append(dx[i+1] / dt[i+1])
		
	
		vy.append(dy[i+1] / dt[i+1])
		

		v.append(ds[i+1] / dt[i+1])
		
		dvx.append(vx[i+1] - vx[i])
		dvy.append(vy[i+1] - vy[i])
		dv.append(math.fabs(v[i+1] - vy[i]))

		a.append(dv[i+1] / dt[i+1])
		
		jerk.append((a[i+1] - a[i]) / dt[i+1])
		
strokes += 1
stroke_locations.append(size-1)
#Initial Feature Analysis, broken up by strokes

for j in range(strokes - 1) :
	print(events_complex[j])
	loc = stroke_locations[j+1]	#next stroke loc
	cur_loc = stroke_locations[j] #current stroke loc
	cur_size = loc - cur_loc		#size of current stroke
	if j != 0 :
		dy_temp = int(ypos[cur_loc + 1]) - int(ypos[cur_loc])
		dx_temp = int(xpos[cur_loc + 1]) - int(xpos[cur_loc])
		dt_temp = timestamp[cur_loc + 1] - timestamp[cur_loc]
		angle_min.append(angle[cur_loc+1])
		angle_max.append(angle[cur_loc+1])
		angle_mean.append(0)
		angle_sd.append(0)
		angle_minmax.append(0)
		angle_v_min.append(angle_v[cur_loc+1])
		angle_v_max.append(angle_v[cur_loc+1])
		angle_v_mean.append(0)
		angle_v_sd.append(0)
		angle_v_minmax.append(0)
		curve_min.append(curve[cur_loc+1])
		curve_max.append(curve[cur_loc+1])
		curve_mean.append(0)
		curve_sd.append(0)
		curve_minmax.append(0)
		curve_r_min.append(curve_r[cur_loc+1])
		curve_r_max.append(curve_r[cur_loc+1])
		curve_r_mean.append(0)
		curve_r_sd.append(0)
		curve_r_minmax.append(0)
		vx_min.append(vx[cur_loc+1])
		vx_max.append(vx[cur_loc+1])
		vx_mean.append(0)	
		vx_sd.append(0)
		vx_minmax.append(0)
		vy_min.append(vy[cur_loc+1])
		vy_max.append(vy[cur_loc+1])
		vy_mean.append(0)
		vy_sd.append(0)
		vy_minmax.append(0)
		v_min.append(v[cur_loc+1])
		v_max.append(v[cur_loc+1])
		v_mean.append(0)
		v_sd.append(0)
		v_minmax.append(0)
		a_min.append(a[cur_loc+1])
		a_max.append(a[cur_loc+1])
		a_mean.append(0)
		a_sd.append(0)
		a_minmax.append(0)
		jerk_min.append(jerk[cur_loc+1])
		jerk_max.append(jerk[cur_loc+1])
		jerk_mean.append(0)
		jerk_sd.append(0)
		jerk_minmax.append(0)
		critical_points.append(0)
		straightness.append(0)
		jitter.append(0)
		total_distance.append(0)
		
	for i in range(loc - 1):
		
		if angle[i+1] < angle_min[j] :
			angle_min[j] = angle[i+1]
		elif angle[i+1] > angle_max[j] :
			angle_max[j] = angle[i+1]
		angle_mean[j] += angle[i+1]
		
		if angle_v[i+1] < angle_v_min[j] :
			angle_v_min[j] = angle_v[i+1]
		elif angle_v[i+1] > angle_v_max[j] :
			angle_v_max[j] = angle_v[i+1]
		angle_v_mean[j] += angle_v[i+1]
		
		if curve[i+1] < curve_min[j] :
				curve_min[j] = curve[i+1]
		elif curve[i+1] > curve_max[j] :
			curve_max[j] = curve[i+1]
		curve_mean[j] += curve[i+1]
		
		if curve_r[i+1] < curve_r_min[j] :
			curve_r_min[j] = curve_r[i+1]
		elif curve_r[i+1] > curve_r_max[j] :
			curve_r_max[j] = curve_r[i+1]
		curve_r_mean[j] += curve_r[i+1]
		if curve_r[i+1] == 0 and math.fabs(curve[i+1]) > (math.pi / 10) :
			critical_points[j] += 1
		
		if vx[i+1] < vx_min[j] :
			vx_min[j] = vx[i+1]
		elif vx[i+1] > vx_max[j] :
			vx_max[j] = vx[i+1]
		vx_mean[j] += vx[i+1]
		
		if vy[i+1] < vy_min[j] :
			vy_min[j] = vy[i+1]
		elif vy[i+1] > vy_max[j] :
			vy_max[j] = vy[i+1]
		vy_mean[j] += vy[i+1]
		
		if v[i+1] < v_min[j] :
			v_min[j] = v[i+1]
		elif v[i+1] > v_max[j] :
			v_max[j] = v[i+1]
		v_mean[j] += v[i+1]
		
		if a[i+1] < a_min[j] :
			a_min[j] = a[i+1]
		elif a[i+1] > a_max[j] :
			a_max[j] = a[i+1]
		a_mean[j] += a[i+1]
		
		if jerk[i+1] < jerk_min[j] :
			jerk_min[j] = jerk[i+1]
		elif jerk[i+1] > jerk_max[j] :
			jerk_max[j] = jerk[i+1]
		jerk_mean[j] += jerk[i+1]
		
		total_distance[j] += ds[i+1]
		
	#x_mean[j] = x_mean[j]/(cur_size - 1)
	#x_minmax[j] = x_max[j] - x_min[j]

	#y_mean[j] = y_mean[j]/(cur_size - 1)
	#y_minmax[j] = y_max[j] - y_min[j]
	
	angle_mean[j] = angle_mean[j]/(cur_size)
	angle_minmax[j] = angle_max[j] - angle_min[j]

	angle_v_mean[j] = angle_v_mean[j]/(cur_size)
	angle_v_minmax[j] = angle_v_max[j] - angle_v_min[j]

	curve_mean[j] = curve_mean[j]/(cur_size)
	curve_minmax[j] = curve_max[j] - curve_min[j]

	curve_r_mean[j] = curve_r_mean[j]/(cur_size)
	curve_r_minmax[j] = curve_r_max[j] - curve_r_min[j]

	vx_mean[j] = vx_mean[j]/(cur_size)
	vx_minmax[j] = vx_max[j] - vx_min[j]

	vy_mean[j] = vy_mean[j]/(cur_size)
	vy_minmax[j] = vy_max[j] - vy_min[j]

	v_mean[j] = v_mean[j]/(cur_size)
	v_minmax[j] = v_max[j] - v_min[j]

	a_mean[j] = a_mean[j]/(cur_size)
	a_minmax[j] = a_max[j] - a_min[j]

	jerk_mean[j] = jerk_mean[j]/(cur_size)
	jerk_minmax[j] = jerk_max[j] - jerk_min[j]
	total_dx = xpos[loc] - xpos[cur_loc]
	total_dy = ypos[loc] - ypos[cur_loc]
	
	straightness[j] = math.sqrt((total_dx ** 2) + (total_dy ** 2))/total_distance[j]

	for i in range (cur_size) :
		#x_sd += ((xpos[i+1] - x_mean) ** 2)
		#y_sd += ((ypos[i+1] - y_mean) ** 2)
		#changing next spot from size to loc
		angle_sd[j] += ((angle[i+cur_loc] - angle_mean[j]) ** 2)
		angle_v_sd[j] += ((angle_v[i+cur_loc] - angle_v_mean[j]) ** 2)
		curve_sd[j] += ((curve[i+cur_loc] - curve_mean[j]) ** 2)
		curve_r_sd[j] += ((curve_r[i+cur_loc] - curve_r_mean[j]) ** 2)
		vx_sd[j] += ((vx[i+cur_loc] - vx_mean[j]) ** 2)
		vy_sd[j] += ((vy[i+cur_loc] - vy_mean[j]) ** 2)
		v_sd[j] += ((v[i+cur_loc] - v_mean[j]) ** 2)
		a_sd[j] += ((a[i+cur_loc] - a_mean[j]) ** 2)
		jerk_sd[j] += ((jerk[i+cur_loc] - jerk_mean[j]) ** 2)
	
	#x_sd[j] = math.sqrt(x_sd/(size-1))
	#y_sd[j] = math.sqrt(y_sd/(size-1))
	angle_sd[j] = math.sqrt(angle_sd[j]/(cur_size))
	angle_v_sd[j] = math.sqrt(angle_v_sd[j]/(cur_size))
	curve_sd[j] = math.sqrt(curve_sd[j]/(cur_size))
	curve_r_sd[j] = math.sqrt(curve_r_sd[j]/(cur_size))
	vx_sd[j] = math.sqrt(vx_sd[j]/(cur_size))
	vy_sd[j] = math.sqrt(vy_sd[j]/(cur_size))
	v_sd[j] = math.sqrt(v_sd[j]/(cur_size))
	a_sd[j] = math.sqrt(a_sd[j]/(cur_size))	
	jerk_sd[j] = math.sqrt(jerk_sd[j]/(cur_size))
	
# write features to output file
with open('mouse_features.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for j in range(strokes-1) :
		writer.writerow([events_complex[j], critical_points[j], straightness[j], total_distance[j],
						angle_max[j], angle_min[j], angle_minmax[j], angle_mean[j], angle_sd[j],
						angle_v_max[j], angle_v_min[j], angle_v_minmax[j], angle_v_mean[j], angle_v_sd[j], 
						curve_max[j], curve_min[j], curve_minmax[j], curve_mean[j], curve_sd[j], 
						curve_r_max[j], curve_r_min[j], curve_r_minmax[j], curve_r_mean[j], curve_r_sd[j], 
						vx_max[j], vx_min[j], vx_minmax[j], vx_mean[j], vx_sd[j], 
						vy_max[j], vy_min[j], vy_minmax[j], vy_mean[j], vy_sd[j], 
						v_max[j], v_min[j], v_minmax[j], v_mean[j], v_sd[j], 
						a_max[j], a_min[j], a_minmax[j], a_mean[j], a_sd[j], 
						jerk_max[j], jerk_min[j], jerk_minmax[j], jerk_mean[j], jerk_sd[j]])

	
#main()