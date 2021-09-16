export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    try {
      throw new Error('cannot divide by 0')
    } catch (error) {
      return error
    }
  } else {
    return numerator / denominator
  }
}
