import { uploadPhoto, createUser } from './utils';

export default function asyncUploadUser() {
  let object;
  try {
    const valueUpload = await uploadPhoto();
    const valueUser = await createUser();
    object = {
      photo: valueUpload,
      user: valueUser,
    };
    return object;
  } catch {
    object = {
      photo: null,
      user: null,
    };
  }

  return object;
}
