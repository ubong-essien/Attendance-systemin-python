def compute_stop_positions():
    import math
    from math import sin

    Stop_positions = []
    Nsp = 0
    Psp=0
    cam_fov = 90 # in degrees
    rail_lenght = 100 #in meters
    max_obj_distance = 15 # in meters
    half_fov= cam_fov/2
    n = 90 - half_fov
    r = sin(math.radians(n))
    initial_pos =  max_obj_distance * sin(math.radians(half_fov)) / sin(math.radians(n))

    r_initial_pos = round(initial_pos)
    Psp = r_initial_pos
   # print(r_initial_pos)
    Stop_positions.append(r_initial_pos)

    #print(Stop_positions)
    Nsp = r_initial_pos + 0.5*r_initial_pos
    Stop_positions.append(round(Nsp))

    #print(round(Nsp))
    while Nsp < rail_lenght:
        Psp = Nsp
        Nsp = Psp + round(0.5*Psp)
        if Nsp < rail_lenght:
            Stop_positions.append(round(Nsp))
        Psp += Nsp
   # print(Stop_positions)
    return Stop_positions

#implement the movement
cur_location = 0
stop_pos = compute_stop_positions()


for position in stop_pos:
    cur_location = position
    if cur_location == position:
        #move camera to the position
        print("Camera is at " + str(cur_location))
       # stop camera
        #take snap shot
        continue
   
    #