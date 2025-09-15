module.exports = {
    apps : [{
      name   : "automacao-adaptacao-curriculos-backend",
      script : "run.py",
      interpreter: "pipenv",
      interpreter_args: "run python",
      env_production: {
        ENVIRONMENT: "production",
        FLASK_ENV: "production",
        FLASK_APP: "app.py",
        PYTHONPATH: "."
      },
      env_development: {
        ENVIRONMENT: "development", 
        FLASK_ENV: "development",
        FLASK_APP: "app.py",
        PYTHONPATH: "."
      },
      autorestart: true,
      watch: false,
      max_memory_restart: "1G",
      error_file: "./logs/err.log",
      out_file: "./logs/out.log",
      log_file: "./logs/combined.log",
      time: true,
      log_date_format: "YYYY-MM-DD HH:mm:ss Z",
      merge_logs: true,
      max_restarts: 10,
      min_uptime: "10s",
      restart_delay: 4000
    }]
  }
