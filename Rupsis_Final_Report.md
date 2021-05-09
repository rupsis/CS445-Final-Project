Name (netid): Nathaniel Rupsis (nrupsis2)
# CS 445 - Final Project: Blender Tour Into The Picture

## Motivation and impact: Why did you choose this topic? What is the more general importance or impact?
I chose to implement the tour into the photo paper because I wanted an automatic way to bring my images to life. It's difficult to argue the "importance" of 2D image to 3D animation for this project, since the motivation is bring images to life for artistic purposes. This method could however be built upon, and used for something more useful (crime scene reconstruction, inserting objects into a 3D scene, etc).

## Approach
The approach I took to implement the "tour into the picture" was pretty much how it's implemented in the paper (from a conceptual standpoint). The first step was to create a grid system for the user to be able to set boundaries for:


Once the guide has been created, the user is then able to position the coordinates to create the back plane of the single point perspective, and set the vanishing point:

![image](./paper_images/getting_depth.png)

Once the user has finished their input, a script is executed to calculate the depth of the image based on the uses input and focal length (if available, else it's guessed). The method for obtaining the image depth is via similar triangles. (slide taken from lecture):

![image](./paper_images/getting_depth.png)

Once the depth has been calculated, the original guide mesh is then transformed into a 3D object, and the texture image is then UV projected onto it, creating a 3D representation of our image. 



 Results: Explain your results and their significance

 Implementation details: Provide details, such as programming language, packages, etc. Include
a list of any external resources used, such as open source code and data.

## Challenge / innovation: 
The largest challenge in this project was learning how the blender programming system worked. Blender provides a incredibly rich toolset for creating 3D graphic, however, their python API documentation is lacking... A majority of the time spent was figuring out how to achieve something within blender. 


Describe what you think was challenging or innovative about your
project. Explain the effort required to interpret unclear steps to a paper’s implementation or get a proposed new idea to work. Write and justify how many points you expect to receive for the challenge/innovation component of grading.
## Future work
This project is still in it's infancy. While we were able to achieve some decent results with the current implementation, it's not super intuitive or user friendly. The next step for this project would be to move the sequence of scripts into a collection of UI elements. Additionally, for adding in foreground objects, I would love it if the user was able to draw object boundaries, rather than having to create a bounding box (Exp below)



## Credit 
* [Blender](https://www.blender.org/)
* [Train Tracks](http://orthographic.weebly.com/uploads/1/7/3/2/17321634/8720148_orig.jpg)
* [City](https://artprojectsforkids.org/draw-a-city-with-one-point-perspective/)