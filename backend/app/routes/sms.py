from flask import Blueprint
from app.services import DataIngestionService

sms_blueprint = Blueprint('sms_blueprint', __name__)
data_ingestion_service = DataIngestionService()

@sms_blueprint.route('/sms', methods=['POST'])
def handle_sms():
    return data_ingestion_service.ingest_sms()