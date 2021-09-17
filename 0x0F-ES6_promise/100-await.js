import { uploadPhoto, createUser } from './utils';

export default function asyncUploadUser() {
  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((result) => ({
      photo: result[0].value,
      user: result[1].value,
    })).catch(() => ({
      photo: null,
      user: null,
    }));
}
