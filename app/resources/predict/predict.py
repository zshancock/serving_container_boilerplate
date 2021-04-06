import falcon
from app.resources.predict.helpers import double_value


class PredictionResource:
    """Falcon resource that handles the prediction."""
    def on_post(self, req, resp):
        try:
            # Retrieve request.
            body = req.media.get("request")

            # Perform model prediction, double_value is placeholder.
            prediction = double_value(body)

            # Prepare response.
            resp.status = falcon.HTTP_200
            resp.media = {
                "prediction": prediction,
                }

        except Exception as e:
            # Return payload for failed request.
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
