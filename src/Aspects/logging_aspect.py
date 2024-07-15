from src.Aspects.aspect_interface import AspectInterface


class LoggingAspect(AspectInterface):
    def aspect_logic_implementation(self):
        return "Logging ... User wants to add a product."
