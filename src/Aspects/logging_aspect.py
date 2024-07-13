from src.Aspects.aspect_interface import AspectInterface


class LoggingAspect(AspectInterface):
    def aspect_task(self):
        return "Logging ... User wants to add a product."
