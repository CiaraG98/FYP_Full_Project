from google.cloud import storage

client = storage.Client.from_service_account_json('./bucket_access_key/im-a-celebrity-fyp-f43156a39151.json')
bucket = client.get_bucket('celeb_model')

blob = bucket.get_blob("2f5114b5eb72f9515802779c42c1b289bebdb1cfc8ce94c653237518eb530b34.75f2a4fe69178ff43138117a977e107a5fc7d402603a0825a296b531f246b3f2")
MODEL_DIR = "./tempdir/model_/model.75f2a4fe69178ff43138117a977e107a5fc7d402603a0825a296b531f246b3f2"

def get_model():
    print("Download fine-tuned model...")
    bucket = client.get_bucket('celeb_model')
    blob = bucket.get_blob("2f5114b5eb72f9515802779c42c1b289bebdb1cfc8ce94c653237518eb530b34.75f2a4fe69178ff43138117a977e107a5fc7d402603a0825a296b531f246b3f2")
    blob.download_to_filename(MODEL_DIR)
    print("Done :)")
