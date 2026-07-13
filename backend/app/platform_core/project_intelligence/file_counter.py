class ProjectFileCounter:
    def count(self):
        return {
            "ready": True,
            "completed_files": 0,
            "remaining_files": 0,
            "scan_mode": "contract_only",
            "source": "project_file_counter",
        }

project_file_counter = ProjectFileCounter()
