from src.Aspects.aspect_interface import AspectInterface


class AuthenticationAspect(AspectInterface):
    def aspect_logic_implementation(self):
        return "User has privileges."
