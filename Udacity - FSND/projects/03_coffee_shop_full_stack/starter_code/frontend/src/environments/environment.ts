
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'dev-8d5ayvrx.eu.auth0.com', // the auth0 domain prefix
    audience: 'https://dev-8d5ayvrx.eu.auth0.com/api/v2/', // the audience set for the auth0 app
    clientId: '5sc381laMcUPwDVQyt8dthYV0YHUWVKB', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:4200', // the base url of the running ionic application. 
  }
};
