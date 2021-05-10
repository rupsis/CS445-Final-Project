import bpy
bpy.app.debug = True

mesh_name = "image_guide"

# aspect ratio for the image
aspect_ratio = (15, 9)

outside_verts = [
    (0,0,0), 
    (aspect_ratio[0],0,0),
    (0,aspect_ratio[1],0),
    (aspect_ratio[0],aspect_ratio[1],0)
]

ar_x_third = int(aspect_ratio[0] / 3)
ar_y_third = int(aspect_ratio[1] / 3)

inside_verts = [
    (ar_x_third, ar_y_third,0), 
    ( aspect_ratio[0] - ar_x_third, ar_y_third, 0),
    (aspect_ratio[0] - ar_x_third, aspect_ratio[1] - ar_y_third,0),
    (ar_x_third, aspect_ratio[1] - ar_y_third,0)
]

center_vert = [(aspect_ratio[0]/2, aspect_ratio[1]/2 ,0)]


connecting_edges=[
    (4,8),
    (5,8),
    (6,8),
    (7,8)
]

outer_faces = [
    (0, 4, 7, 2),
    (0, 1 ,5 ,4),
    (1, 3, 6, 5),
    (3, 2, 7, 6)
]

inner_faces = [
    (4, 5, 6,7)
]

verts = outside_verts + inside_verts + center_vert
edges = connecting_edges
faces = outer_faces + inner_faces


mesh = bpy.data.meshes.new(mesh_name)
mesh.from_pydata(verts, edges, faces)

obj = bpy.data.objects.new(mesh_name, mesh)
scene = bpy.context.scene
scene.collection.objects.link(obj)

