import React from 'react';

function formatTimestamp(ts) {
  if (!ts) return '';
  const date = new Date(ts);
  return date.toLocaleString('en-GB', { timeZone: 'UTC', hour12: true }) + ' UTC';
}

function renderEvent(event) {
  const { author, action, from_branch, to_branch, timestamp } = event;
  if (action === 'PUSH') {
    return (
      <span>
        <b>{author}</b> pushed to <b>{to_branch}</b> on {formatTimestamp(timestamp)}
      </span>
    );
  } else if (action === 'PULL_REQUEST') {
    return (
      <span>
        <b>{author}</b> submitted a pull request from <b>{from_branch}</b> to <b>{to_branch}</b> on {formatTimestamp(timestamp)}
      </span>
    );
  } else if (action === 'MERGE') {
    return (
      <span>
        <b>{author}</b> merged branch <b>{from_branch}</b> to <b>{to_branch}</b> on {formatTimestamp(timestamp)}
      </span>
    );
  } else {
    return <span>Unknown event</span>;
  }
}

const EventList = ({ events, loading }) => {
  if (loading) return <div className="text-center py-8">Loading...</div>;
  if (!events.length) return <div className="text-center py-8">No events found.</div>;
  return (
    <ul className="space-y-4">
      {events.map(event => (
        <li key={event._id} className="bg-white shadow rounded p-4">
          {renderEvent(event)}
        </li>
      ))}
    </ul>
  );
};

export default EventList; 