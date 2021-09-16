export default function handleResponseFromAPI(promise) {
  promise.then(('success') => {
    return {
      status: 200,
      body: 'success',
    };
  }).catch(() => { });
  console.log('Got a response from the API');
}
