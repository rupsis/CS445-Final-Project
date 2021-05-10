import bpy
bpy.app.debug = True

 # load image and uv map from camera
bpy.ops.image.open(
    filepath="//src_images/city.jpg", 
    directory="/Users/P3024012/projects/CS445-Final-Project/src_images/", 
    files=[{"name":"city.jpg", "name":"city.jpg"}], 
    show_multiview=False
) 

def UV_Project(target_object):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')


    # select guide and enter edit mode
    guide.select_set(True)
    print(target_object.name_full)
    bpy.context.view_layer.objects.active = target_object

    # set the view port to the camera and UV project
    bpy.ops.object.editmode_toggle()


    for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_perspective = 'CAMERA'
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.uv.project_from_view(override , camera_bounds=True, correct_aspect=False, scale_to_bounds=False)
       

guide = bpy.data.objects['image_guide']
plane = bpy.data.objects['Plane']

box_verts = [4,5,6,7,8]

focal_length = 0.035
camea_height = 1

# get uv map before object position
UV_Project(plane)

bpy.ops.object.editmode_toggle()

# Normalize to mm
Va_Vo = (guide.data.vertices[8].co[1] - guide.data.vertices[5].co[1]) / 1000

print(Va_Vo)
    
# calculate foreground object depth
Vt_Vb = (plane.data.vertices[3].co[1] - plane.data.vertices[1].co[1]) / 1000
print(Vt_Vb)
hi = (Vt_Vb / Va_Vo) * camea_height
print(hi)
obj_depth = hi * (focal_length / Vt_Vb)
print(obj_depth)
for i in range(4):
    plane.data.vertices[i].co.z = -(obj_depth / 10)
    