import falcon
from app.resources.predict.predict import PredictionResource


class HealthResource:
    """Health check."""
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = "Healthy"


# Assemble the API Service.
api = falcon.API()
api.add_route("/health", HealthResource())
api.add_route("/predict", PredictionResource())
