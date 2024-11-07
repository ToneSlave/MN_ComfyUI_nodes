import comfyui
import numpy as np
import cv2
from PIL import Image
import io

# Define the node class
class SimpleGrayscaleNode(comfyui.ComfyNode):
    def __init__(self):
        super().__init__()

    def process(self, input_image: np.array):
        """
        This method will process the input image and convert it to grayscale.
        :param input_image: The input image as a NumPy array.
        :return: Processed grayscale image.
        """
        # Convert the image to grayscale using OpenCV
        grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        # Convert it back to a format compatible with PIL
        return Image.fromarray(grayscale_image)

    def execute(self, inputs: dict) -> dict:
        """
        This is the execution method of the node.
        It takes the input image and applies the grayscale filter.
        :param inputs: Input dictionary containing input data.
        :return: Output dictionary containing processed data.
        """
        # Get the input image from the input dictionary
        input_image = inputs.get('image')
        
        if input_image is not None:
            # Process the image and return the result
            output_image = self.process(input_image)
            return {'grayscale_image': output_image}
        else:
            raise ValueError("No input image provided!")

# Register the node with ComfyUI
comfyui.register_node('SimpleGrayscaleNode', SimpleGrayscaleNode)
