import bpy
bpy.app.debug = True

mesh_name = "image_guide"

guide = bpy.data.objects['image_guide']
camera = bpy.data.objects['Camera']

box_verts = [4,5,6,7,8]

focal_length = 0.035
camea_height = 1


# Normalize to mm
Va_Vo = (guide.data.vertices[8].co[1] - guide.data.vertices[5].co[1]) / 1000

# calculate the height of the camera
depth = camea_height * (focal_length / Va_Vo)

print(depth)


for v in box_verts:
    guide.data.vertices[v].co.z = -depth
    
# Center camera on image plane
camera.location = (
    guide.data.vertices[8].co.x, 
    guide.data.vertices[8].co.y, 
    (depth / 2) + 2
)
camera.rotation_euler = (0, 0, 0)

# load image and uv map from camera
bpy.ops.image.open(
    filepath="//src_images/city.jpg", 
    directory="/Users/P3024012/projects/CS445-Final-Project/src_images/", 
    files=[{"name":"city.jpg", "name":"city.jpg"}], 
    show_multiview=False
)


# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')


# select guide and enter edit mode
guide.select_set(True)
bpy.context.view_layer.objects.active = guide

# set the view port to the camera and UV project
bpy.ops.object.editmode_toggle()


for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            for region in area.regions:
                if region.type == 'WINDOW':
                    override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                    bpy.ops.uv.project_from_view(override , camera_bounds=False, correct_aspect=True, scale_to_bounds=True)

# exit edit mode
bpy.ops.object.editmode_toggle()

# apply material and texture
material = bpy.data.materials.get("Material")
if material is None:
    material = bpy.data.materials.new(name="Material")

material.use_nodes = True
bsdf = material.node_tree.nodes["Principled BSDF"]
image_texture = material.node_tree.nodes.new('ShaderNodeTexImage')
image_texture.image = bpy.data.images.get('city.jpg') # bpy.data.images.load("/Users/P3024012/projects/CS445-Final-Project/src_images/")
material.node_tree.links.new(bsdf.inputs['Base Color'], image_texture.outputs['Color'])
    
if guide.data.materials:
    guide.data.materials[0] = material
else:
    guide.data.materials.append(material)