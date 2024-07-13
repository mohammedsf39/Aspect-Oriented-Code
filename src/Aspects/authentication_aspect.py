from src.Aspects.aspect_interface import AspectInterface


class AuthenticationAspect(AspectInterface):
    def aspect_task(self):
        return "User has privileges."
