# Flask Monitoring Stack Project 🚀

This project demonstrates full-stack observability and monitoring for a simple Python Flask application using:

- **Prometheus** & **Grafana** → Metrics monitoring
- **Filebeat**, **Logstash**, **Elasticsearch**, and **Kibana (ELK Stack)** → Log collection and visualization

---

## 🔧 Tech Stack

| Tool           | Purpose                                 |
|----------------|------------------------------------------|
| Flask          | Python web app (metrics + logs enabled)  |
| Prometheus     | Scrapes app and node metrics             |
| Grafana        | Visualizes Prometheus metrics            |
| Filebeat       | Ships structured app logs                |
| Logstash       | Parses & sends logs to Elasticsearch     |
| Elasticsearch  | Stores structured logs                   |
| Kibana         | Visualizes logs (heatmaps, filters, etc) |

---

## 🏗️ Project Structure

monitoring-stack-project/
├── app.py # Flask application
├── Dockerfile # Dockerize the Flask app
├── filebeat.yml # Filebeat config
├── filebeat-pipeline.conf # Logstash pipeline config
├── flask-deployment.yaml # K8s Deployment (Optional)
├── prometheus.yml # Prometheus targets
├── app.log / prometheus.log # Log files
└── elk/, grafana/, prometheus/ # Tool-specific configs

yaml
Copy
Edit

---

## ▶️ How to Run

### 1. Start Flask App
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
2. Start Prometheus & Node Exporter
bash
Copy
Edit
./prometheus/prometheus --config.file=prometheus.yml &
./node_exporter &
3. Start Grafana
Run Grafana service (or use Docker Desktop)

Add Prometheus as a data source

Import dashboards or create custom ones

4. Start ELK Stack
bash
Copy
Edit
sudo systemctl start elasticsearch
sudo systemctl start logstash
sudo systemctl start kibana
5. Start Filebeat
bash
Copy
Edit
sudo filebeat -e -c filebeat.yml
📊 Visualizations
✅ In Grafana:
CPU & memory metrics from node_exporter

Flask app request latency

Custom dashboards via PromQL

✅ In Kibana:
Log heatmaps (error, info, warn)

Search logs by endpoints

Filter logs by level, path, timestamp

📸 Screenshots
Include screenshots here of:

Prometheus Targets

Grafana dashboards

Kibana heatmaps or log search

💡 Highlights
Full-stack monitoring in one place

Clean structured logging for production-ready apps

Easy integration with Kubernetes or Dockerized environments

Demonstrates real-world DevOps monitoring pipelines

📂 Portfolio Note
This project is part of my DevOps portfolio.
Check out my portfolio site for more projects!

🙌 Author
Aishwarya Govindkar
DevOps Engineer | Cloud Enthusiast
