
import uvicorn

import os
from app.EmailProvider import EmailProvider
from app.provider.Provider_sendgrid import Provider_sendgrid

app = FastAPI()
app.include_router(email.router)

lsfastapi.Wrapper(app, init_mongoengine=False)
eswebapi.initClients(webapispec=webapispec)
providers = ["SENDGRID"]

provider = os.environ.get("EMAIL_PROVIDER", "SENDGRID")
if provider not in providers:
	raise Exception("provider not found")

EmailProvider.provider = Provider_sendgrid()

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=9000, log_level="info", reload=True)
