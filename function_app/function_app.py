import azure.functions as func
import logging
import random

# Create the FunctionApp
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered function to simulate a random deployment approval check.
    Returns a decision ("Approved" or "Not Approved") as the response.
    """
    logging.info('Python HTTP trigger function is processing a deployment approval check.')

    # Simulate random approval decision
    decision = random.choice(["Approved", "Not Approved"])
    logging.info(f"Random approval decision: {decision}")

    # Return the response
    if decision == "Approved":
        return func.HttpResponse(
            decision,
            status_code=200
        )
    else:
        return func.HttpResponse(
            decision,
            status_code=400
        )
