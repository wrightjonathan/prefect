"""
Tasks for interacting with various Kubernetes API objects.

Note that depending on how you choose to authenticate, tasks in this collection might require
a Prefect Secret called `"KUBERNETES_API_KEY"` that stores your Kubernetes API Key;
this Secret must be a string and in BearerToken format.
"""
try:
    from prefect.tasks.kubernetes.deployment import (
        CreateNamespacedDeployment,
        DeleteNamespacedDeployment,
        ListNamespacedDeployment,
        PatchNamespacedDeployment,
        ReadNamespacedDeployment,
        ReplaceNamespacedDeployment,
    )
    from prefect.tasks.kubernetes.job import (
        CreateNamespacedJob,
        DeleteNamespacedJob,
        ListNamespacedJob,
        PatchNamespacedJob,
        ReadNamespacedJob,
        ReplaceNamespacedJob,
        RunNamespacedJob,
    )
    from prefect.tasks.kubernetes.pod import (
        ConnectGetNamespacedPodExec,
        CreateNamespacedPod,
        DeleteNamespacedPod,
        ListNamespacedPod,
        PatchNamespacedPod,
        ReadNamespacedPod,
        ReplaceNamespacedPod,
        ReadNamespacedPodLogs,
    )
    from prefect.tasks.kubernetes.service import (
        CreateNamespacedService,
        DeleteNamespacedService,
        ListNamespacedService,
        PatchNamespacedService,
        ReadNamespacedService,
        ReplaceNamespacedService,
    )
except ImportError as err:
    raise ImportError(
        'Using `prefect.tasks.kubernetes` requires Prefect to be installed with the "kubernetes" extra.'
    ) from err
