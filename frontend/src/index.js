import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Customer from './components/Customers';
import {createBrowserRouter, RouterProvider} from 'react-router-dom';
import ErrorPage from './utils/errorNotFound';

const root = ReactDOM.createRoot(document.getElementById('root'));

const router = createBrowserRouter(
  [{
    path: "/",
    element: <Customer />,
    errorElement: <ErrorPage />,
  },
  {
    children: [
      {
        path: "accounts/:accountId/",
        element: <App />
      }
    ]
  }
  ])

root.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);

