import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promisePhoto = uploadPhoto();
  const promiseUser = createUser();
  const promises = [promisePhoto, promiseUser];
  Promise.allSettled(promises)
    .then((results) => {
      console.log(results[0].value.body, results[1].value.firstName, results[1].value.lastName);
    });
}
