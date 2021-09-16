import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUp = await signUpUser(firstName, lastName)
    .then((response) => ({
      status: 'fulfilled',
      value: response,
    }))
    .catch((error) => ({
      status: 'rejected',
      value: error.toString(),
    }));
  const upload = await uploadPhoto(fileName)
    .catch((error) => ({
      status: 'rejected',
      value: error.toString(),
    }));

  return [signUp, upload];
}
