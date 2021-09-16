import { uploadPhoto, createUser } from './utils';

const promisePhoto = uploadPhoto();
const promiseUser = createUser();

export default function handleProfileSignup() {
  const promises = [promisePhoto, promiseUser];
  return Promise.all(promises)
    .then((results) => {
      console.log(results[0].body + " " + results[1].firstName + " " + results[1].lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}