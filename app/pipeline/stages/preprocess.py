from app.pipeline.pipeline import PipelineStage

class ImagePreprocessor(PipelineStage):

    def process(self, image):

        print("Preprocessing image")

        return image
