from uvicorn import run

if __name__ == "__main__":
    run(
        "app.adapters.inbound.rest.main:app",
        host="0.0.0.0",
        port=8010,
        workers=1,
        use_colors=True,
        reload=True,
    )
