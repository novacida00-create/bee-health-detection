function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString('id-ID');
}

function getStatusColor(status) {
    const colors = {
        'healthy': '#28a745',
        'warning': '#ffc107',
        'danger': '#dc3545'
    };
    return colors[status] || '#6c757d';
}

function showToast(message, type) {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 5000);
}

async function apiCall(url, method = 'GET', body = null) {
    const options = {
        method,
        headers: {}
    };
    if (body) {
        options.body = body;
    }
    const response = await fetch(url, options);
    return await response.json();
}
