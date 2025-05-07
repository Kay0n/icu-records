from app import create_app 


if __name__ == "__main__":
    app = create_app()
    app.logger.info(f"Starting Flask development server")
    app.run(host="localhost", port=50000, debug=True)