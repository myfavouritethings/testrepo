import React, { useState, useEffect } from 'react';

function HealthCheck() {
  const [status, setStatus] = useState('checking...');

  useEffect(() => {
    fetch('/api/health')
      .then(response => response.json())
      .then(data => setStatus(data.status))
      .catch(error => {
        console.error('Error fetching health check:', error);
        setStatus('error');
      });
  }, []);

  return (
    <div>
      <p>Backend Status: {status}</p>
    </div>
  );
}

export default HealthCheck;
