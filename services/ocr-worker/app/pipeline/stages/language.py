from app.pipeline.pipeline import PipelineStage

class LanguageDetectorStage(PipelineStage):

    def process(self, text):

        return "unknown"
