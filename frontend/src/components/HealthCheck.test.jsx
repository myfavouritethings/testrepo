import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import HealthCheck from './HealthCheck';

// Mock the fetch function
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ status: 'ok' }),
  })
);

beforeEach(() => {
    fetch.mockClear();
  });

test('renders HealthCheck component and fetches status', async () => {
  render(<HealthCheck />);
  
  // Initially, it should show "checking..."
  expect(screen.getByText(/Backend Status: checking.../i)).toBeInTheDocument();

  // Wait for the fetch call to complete and the component to re-render
  await waitFor(() => {
    expect(screen.getByText(/Backend Status: ok/i)).toBeInTheDocument();
  });

  // Verify that fetch was called
  expect(fetch).toHaveBeenCalledWith('/api/health');
});
