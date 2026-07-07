from androguard.misc import AnalyzeAPK
import hashlib
import os


def sha256(file_path):
    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)

            if not chunk:
                break

            h.update(chunk)

    return h.hexdigest()


def extract_features(apk_path):

    try:

        a, d, dx = AnalyzeAPK(apk_path)

        info = {}

        info["package"] = a.get_package()

        info["permissions"] = a.get_permissions()

        info["activities"] = a.get_activities()

        info["services"] = a.get_services()

        info["receivers"] = a.get_receivers()

        info["providers"] = a.get_providers()

        info["target_sdk"] = a.get_target_sdk_version()

        info["min_sdk"] = a.get_min_sdk_version()

        info["apk_size"] = round(os.path.getsize(apk_path) / (1024 * 1024), 2)

        info["sha256"] = sha256(apk_path)

        return info

    except Exception as e:

        return {
            "error": str(e)
        }