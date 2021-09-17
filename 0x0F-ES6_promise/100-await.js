import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let object;
  try {
    const valueUpload = await uploadPhoto();
    const valueUser = await createUser();
    object = {
      photo: valueUpload,
      user: valueUser,
    };
    return object;
  } catch (err) {
    object = {
      photo: null,
      user: null,
    };
  }

  return object;
}
