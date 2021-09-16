import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending',
  };
  const promise2 = {
    status: 'pending',
  };

  try {
    const signUp = await signUpUser(firstName, lastName);
    promise1.status = 'fulfilled';
    promise1.value = signUp;
  } catch (error) {
    promise1.status = 'reject';
    promise1.value = error.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    promise2.status = 'fulfilled';
    promise2.value = upload;
  } catch (error) {
    promise2.status = 'reject';
    promise2.value = error.toString();
  }

  return [promise1, promise2];
}
