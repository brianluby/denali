ALTER TABLE connection_collection_job
    DROP CONSTRAINT IF EXISTS connection_collection_job_collection_kind_check;

ALTER TABLE connection_collection_job
    ADD CONSTRAINT connection_collection_job_collection_kind_check
    CHECK (
        collection_kind IN (
            'entra_ai',
            'aws_deployments',
            'aws_agent_runtime',
            'azure_deployments',
            'azure_agent_runtime',
            'gcp_deployments',
            'github_source',
            'azure_repos_source',
            'google_workspace_ai'
        )
    );
