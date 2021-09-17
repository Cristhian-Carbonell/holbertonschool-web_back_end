import { uploadPhoto, createUser } from './utils';

export default function asyncUploadUser() {
  const functionPromise = async () => {
    const valueUpload = await uploadPhoto();
    const valueUser = await createUser();
    const object = {
      photo: valueUpload,
      user: valueUser,
    };
    return object;
  };
  const object = functionPromise();
  return Promise.resolve(object)
    .then((result) => result)
    .catch(() => ({
      photo: null,
      user: null,
    }));
}
