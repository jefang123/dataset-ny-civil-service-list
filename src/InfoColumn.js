import React from 'react';

export const InfoColumn = ({fieldValue}) => {
  return (
    fieldValue ? 
      <p>
        {fieldValue.name} : {fieldValue.description}
      </p> : null
  )
}