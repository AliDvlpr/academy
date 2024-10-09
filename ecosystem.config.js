amodule.exports = {
  apps: [
    {
      name: "prereg_api",
      script: "manage.py",
      args: "runserver 0.0.0.0:8000",
      interpreter: "python3",
      exec_mode: "fork",
      instances: 1,
      autorestart: true,
      watch: false,
      max_restarts: 15,
    },
  ],
};
