import React from 'react';
import Gallery from 'react-photo-gallery';
import pic1 from '../Image/pic1.jpg';






export default class Sample extends React.Component {
    render() {
	return (
			<Gallery photos={PHOTO_SET} />
	);
    }
}
const PHOTO_SET = [
  {
    src: pic1,
    width: 4,
    height: 3
  },
];