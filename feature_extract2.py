import csv
import math

#def main():
	f = open('mouse_data.csv')
	csv_f = csv.reader(f)
	
	
	entry_id = []
	session_id = []
	timestamp = []
	xpos = []
	ypos = []
	l_mousedown = []
	l_mouseup = []
	r_mousedown = []
	r_mouseup = []
	m_mousedown = []
	m_mouseup = []
	for row in csv_f:
		entry_id.append(row[0])
		session_id.append(row[1])
		timestamp.append(row[2])
		xpos.append(row[3])
		ypos.append(row[4])
		l_mousedown.append(row[5])
		l_mouseup.append(row[6])
		r_mousedown.append(row[7])
		r_mouseup.append(row[8])
		m_mousedown.append(row[9])
		m_mouseup.append(row[10])

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

	ax = [0]
	ay = [0]
	a = [0]

	jerk = [0]

	x_min = xpos[0]
	x_max = xpos[0]
	x_mean = 0
	x_sd = 0
	x_minmax = 0
	y_min = ypos[0]
	y_max = ypos[0]
	y_mean = 0
	y_sd = 0
	y_minmax = 0
	angle_min = atan2(dy_min,dy_min)
	angle_max = atan2(dy_min,dy_min)
	angle_mean = 0
	angle_sd = 0
	angle_minmax = 0
	angle_v_min = (atan2((ypos[2]-ypos[1]),(xpos[2]-xpos[1])) - angle_min) / (timestamp[1] - timestamp[0])
	angle_v_max = angle_v_min
	angle_v_mean = 0
	angle_v_sd = 0
	angle_v_minmax = 0
	curve_min = (atan2((ypos[2]-ypos[1]),(xpos[2]-xpos[1])) - angle_min) / sqrt( ((xpos[1]-xpos[0]) ** 2) + ((ypos[1]-ypos[0]) ** 2))
	curve_max = curve_min
	curve_mean = 0
	curve_sd = 0
	curve_minmax = 0
	curve_r_min = curve_min / sqrt( ((xpos[1]-xpos[0]) ** 2) + ((ypos[1]-ypos[0]) ** 2))	
	curve_r_max = curve_r_min
	curve_r_mean = 0
	curve_r_sd = 0
	curve_r_minmax = 0
	vx_min = (xpos[1]-xpos[0]) / (timestamp[1] - timestamp[0])
	vx_max = vx_min
	vx_mean = 0
	vx_sd = 0
	vx_minmax = 0
	vy_min = (ypos[1]-ypos[0]) / (timestamp[1] - timestamp[0])
	vy_max = vy_min
	vy_mean = 0
	vy_sd = 0
	vy_minmax = 0
	v_min = sqrt(((xpos[1]-xpos[0]) ** 2) + ((ypos[1]-ypos[0]) ** 2) / (timestamp[1] - timestamp[0]))
	v_max = v_min
	v_mean = 0
	v_sd = 0
	v_minmax = 0
	a_min = v_min / (timestamp[1] - timestamp[0])
	a_max = a_min
	a_mean = 0
	a_sd = 0
	a_minmax = 0
	jerk_min = a_min / (timestamp[1] - timestamp[0])
	jerk_max = jerk_min
	jerk_mean = 0
	jerk_sd = 0
	jerk_minmax = 0

	total_distance = 0
	total_time = timestamp[size-1]
	critical_points = 0
	for i in range(size - 1):
		dt.append(timestamp[i+1] - timestamp[i])
		
		dx.append(xpos[i+1] - xpos[i])
		if xpos[i+1] < x_min :
			x_min = xpos[i+1]
		elif xpos[1] > x_max :
			x_max = xpos[i+1]
		x_mean += xpos[i+1]
	
		dy.append(ypos[i+1] - ypos[i])
		if ypos[i+1] < y_min :
			y_min = ypos[i+1]
		elif ypos[i+1] > y_max :
			y_max = ypos[i+1]
		y_mean += ypos[i+1]
	
		ds.append(sqrt(pow(dy[i+1],2) + pow(dx[i+1],2)))
		total_distance += ds[i+1]
		
		angle.append(atan2(dy[i+1],dx[i+1]))
		if angle[i+1] < angle_min :
			angle_min = angle[i+1]
		elif angle[i+1] > angle_max :
			angle_max = angle[i+1]
		angle_mean += angle[i+1]
	
		angle_v.append((angle[i+1] - angle[i]) / dt[i+1])
		if angle_v[i+1] < angle_v_min :
			angle_v_min = angle_v[i+1]
		elif angle_v[i+1] > angle_v_max :
			angle_v_max = angle_v[i+1]
		angle_v_mean += angle_v[i+1]
	
		curve.append((angle[i+1] - angle[i]) / ds[i+1])
		if curve[i+1] < curve_min :
			curve_min = curve[i+1]
		elif curve[i+1] > curve_max :
			curve_max = curve[i+1]
		curve_mean += curve[i+1]
	
		curve_r.append((curve[i+1] - curve[i]) / ds[i+1])
		if curve_r[i+1] < curve_r_min :
			curve_r_min = curve_r[i+1]
		elif curve_r[i+1] > curve_r_max :
			curve_r_max = curve_r[i+1]
		curve_r_mean += curve_r[i+1]
		if curve_r[i+1] == 0 and fabs(curve[i+1]) > (pi / 10) :
			critical_points += 1
	
		vx.append(dx[i+1] / dt[i+1])
		if vx[i+1] < vx_min :
			vx_min = vx[i+1]
		elif vx[i+1] > vx_max :
			vx_max = vx[i+1]
		vx_mean += vx[i+1]
	
		vy.append(dy[i+1] / dt[i+1])
		if vy[i+1] < vy_min :
			vy_min = vy[i+1]
		elif vy[i+1] > vy_max :
			vy_max = vy[i+1]
		vy_mean += vy[i+1]
	
		v.append(ds[i+1] / dt[i+1])
		if v[i+1] < v_min :
			v_min = v[i+1]
		elif v[i+1] > v_max :
			v_max = v[i+1]
		v_mean += v[i+1]
		dvx.append(vx[i+1] - vx[i])
		dvy.append(vy[i+1] - vy[i])
		dv.append(fabs(v[i+1] - vy[i]))
	
		a.append(dv[i+1] / dt[i+1])
		if a[i+1] < a_min :
			a_min = a[i+1]
		elif a[i+1] > a_max :
			a_max = a[i+1]
		a_mean += a[i+1]
	
		jerk.append((a[i+1] - a[i]) / dt[i+1])
		if jerk[i+1] < jerk_min :
			jerk_min = jerk[i+1]
		elif jerk[i+1] > jerk_max :
			jerk_max = jerk[i+1]
		jerk_mean += jerk[i+1]

	#Initial Feature Analysis
	x_mean = x_mean/(size - 1)
	x_minmax = x_max - x_min

	y_mean = y_mean/(size - 1)
	y_minmax = y_max - y_min
	
	angle_mean = angle_mean/(size - 1)
	angle_minmax = angle_max - angle_min

	angle_v_mean = angle_v_mean/(size - 1)
	angle_v_minmax = angle_v_max - angle_v_min

	curve_mean = curve_mean/(size - 1)
	curve_minmax = curve_max - curve_min

	curve_r_mean = curve_r_mean/(size - 1)
	curve_r_minmax = curve_r_max - curve_r_min

	vx_mean = vx_mean/(size - 1)
	vx_minmax = vx_max - vx_min
	
	vy_mean = vy_mean/(size - 1)
	vy_minmax = vy_max - vy_min

	v_mean = v_mean/(size - 1)
	v_minmax = v_max - v_min

	a_mean = a_mean/(size - 1)
	a_minmax = a_max - a_min

	jerk_mean = jerk_mean/(size - 1)
	jerk_minmax = jerk_max - jerk_min
	
#main()